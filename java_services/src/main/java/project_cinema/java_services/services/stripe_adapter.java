package project_cinema.java_services.services;
import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import com.stripe.Stripe;
import com.stripe.exception.StripeException;
import com.stripe.model.PaymentIntent;

import project_cinema.java_services.repositories.payment_repository;

@Service
public class stripe_adapter implements payment_adapter{
    
    @Value("${stripe.key}")
    private String stripe_key;

    @Autowired
    private payment_repository payment_repository;

    @Override
    public String process_payment(Float total_price, String currency, Integer customer_id) {
        Stripe.apiKey = stripe_key;
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("amount", (int) (total_price * 100));
        parameters.put("currency", currency);
        parameters.put("payment_method_types", java.util.List.of("card"));
        parameters.put("confirm", true);
        parameters.put("payment_method", "pm_card_visa");
        parameters.put("return_url", "http://localhost:8001/payment/stripe/success");
        try {
            PaymentIntent payment_intent = PaymentIntent.create(parameters);
            payment_repository.deletOrderByCustomerId(customer_id);
            return "Payment successfully completed, Payment Intent ID: " + payment_intent.getId();
        } catch (StripeException e) {
            return "Error with the payment on Stripe: " + e;
        }
    }
}
