package main

import (
	"encoding/json"
	"fmt"
	"log"
	"math/rand"
	"time"

	"github.com/streadway/amqp"
)

type RideRequest struct {
	PickupLocation string
	DropoffLocation string
}

type RideOffer struct {
	DriverName string
	ETA time.Duration
}

func main() {
	conn, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err != nil {
		log.Fatalf("Failed to connect to RabbitMQ: %s", err)
	}
	defer conn.Close()

	ch, err := conn.Channel()
	if err != nil {
		log.Fatalf("Failed to open a channel: %s", err)
	}
	defer ch.Close()

	err = ch.ExchangeDeclare(
		"ride_requests", // name
		"fanout",        // type
		true,            // durable
		false,           // auto-deleted
		false,           // internal
		false,           // no-wait
		nil,             // arguments
	)
	if err != nil {
		log.Fatalf("Failed to declare an exchange: %s", err)
	}

	q, err := ch.QueueDeclare(
		"",    // name
		false, // durable
		false, // delete when unused
		true,  // exclusive
		false, // no-wait
		nil,   // arguments
	)
	if err != nil {
		log.Fatalf("Failed to declare a queue: %s", err)
	}

	err = ch.QueueBind(
		q.Name,          // queue name
		"",              // routing key
		"ride_requests", // exchange
		false,
		nil,
	)
	if err != nil {
		log.Fatalf("Failed to bind queue to exchange: %s", err)
	}

	msgs, err := ch.Consume(
		q.Name, // queue
		"",     // consumer
		true,   // auto-ack
		false,  // exclusive
		false,  // no-local
		false,  // no-wait
		nil,    // args
	)
	if err != nil {
		log.Fatalf("Failed to register a consumer: %s", err)
	}

	forever := make(chan bool)

	go func() {
		for d := range msgs {
			log.Printf("Received a ride request: %s", d.Body)

			var request RideRequest
			err := json.Unmarshal(d.Body, &request)
			if err != nil {
				log.Printf("Failed to unmarshal ride request: %s", err)
				continue
			}

			offer := createRideOffer()
			log.Printf("Sending ride offer: %s", offer)

			err = ch.Publish(
				"",            // exchange
				d.ReplyTo,     // routing key
				false,         // mandatory
				false,         // immediate
				amqp.Publishing{
					ContentType:   "application/json",
					CorrelationId: d.CorrelationId,
					Body:          []byte(offer),
				})
			if err != nil {
				log.Printf("Failed to publish ride offer: %s", err)
			}
		}
	}()

	log.Printf("Waiting for ride requests...")
	<-forever
}

func createRideOffer() string {
	drivers := []string{"Alice", "Bob", "Charlie", "Dave"}
	driver := drivers[rand.Intn(len(drivers))]

	eta := rand.Intn(10) + 1
	duration := time.Duration(
