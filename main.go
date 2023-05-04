package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func handleWebhook(w http.ResponseWriter, r *http.Request) {
    // Parse the incoming webhook payload
    body, err := ioutil.ReadAll(r.Body)
    if err != nil {
        http.Error(w, "Failed to read request body", http.StatusBadRequest)
        return
    }
    defer r.Body.Close()

    var payment Payment
    if err := json.Unmarshal(body, &payment); err != nil {
        http.Error(w, "Failed to parse request body", http.StatusBadRequest)
        return
    }

    // Handle the payment event
    switch payment.Status {
    case PaymentStatusSuccess:
        // Update your database or trigger business workflows
        fmt.Println("Payment successful:", payment.ID)
    case PaymentStatusRefund:
        // Handle refund event
        fmt.Println("Payment refunded:", payment.ID)
    // Handle other payment statuses here...
    }

    // Return a response to the webhook provider
    w.WriteHeader(http.StatusOK)
}

func main() {
    http.HandleFunc("/webhook", handleWebhook)
    http.ListenAndServe(":8080", nil)
}
