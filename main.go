package main

import (
	"fmt"
	"sync"
)

type Payment struct {
	orderID string
	amount  float64
}

type PaymentService struct {
	payments    map[string]float64
	mu          sync.Mutex
	idempotency map[string]bool
	idempMu     sync.Mutex
}

func NewPaymentService() *PaymentService {
	return &PaymentService{
		payments:    make(map[string]float64),
		idempotency: make(map[string]bool),
	}
}

func (p *PaymentService) ProcessPayment(payment Payment) error {
	// check if the payment has already been processed
	p.idempMu.Lock()
	if p.idempotency[payment.orderID] {
		p.idempMu.Unlock()
		return nil
	}
	p.idempotency[payment.orderID] = true
	p.idempMu.Unlock()

	// process the payment
	p.mu.Lock()
	defer p.mu.Unlock()
	if _, ok := p.payments[payment.orderID]; ok {
		return fmt.Errorf("payment with order ID %s already exists", payment.orderID)
	}
	p.payments[payment.orderID] = payment.amount
	fmt.Printf("Payment processed successfully: %v\n", payment)
	return nil
}

func main() {
	paymentSvc := NewPaymentService()

	// make a payment
	payment := Payment{
		orderID: "12345",
		amount:  50.0,
	}
	if err := paymentSvc.ProcessPayment(payment); err != nil {
		fmt.Printf("Error processing payment: %v\n", err)
	}

	// try to make the same payment again
	if err := paymentSvc.ProcessPayment(payment); err != nil {
		fmt.Printf("Error processing payment: %v\n", err)
	}
}
