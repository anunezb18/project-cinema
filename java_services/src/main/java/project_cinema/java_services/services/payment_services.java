package project_cinema.java_services.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;

import project_cinema.java_services.repositories.payment_repository;

@Service
public class payment_services {
    
    
    private final payment_repository payment_repository;
    private final payment_adapter stripe_adapter;
    private final payment_adapter paypal_adapter;

    @Autowired
    public payment_services(payment_repository payment_repository, payment_adapter stripe_adapter, payment_adapter paypal_adapter){
        this.payment_repository = payment_repository;
        this.stripe_adapter = stripe_adapter;
        this.paypal_adapter = paypal_adapter;
    }

    public Optional<Float> getTotalPricebyCustomerId(@PathVariable("customer_id") Integer customer_id){
        if(customer_id == null || customer_id < 0){
            return Optional.empty();
        }
        else{
            return payment_repository.getTotalPricebyCustomerId(customer_id);
        }
    }

    public String process_payment(String provider, Integer customer_id, String currency){
        Optional<Float> price = getTotalPricebyCustomerId(customer_id);
            if(price.isEmpty()){
                return "The customer doesn't have any orders";
            }
        Float total_price = price.get();

        if("stripe".equalsIgnoreCase(provider)){
            return stripe_adapter.process_payment(total_price, currency, customer_id);
        }
        else if("paypal".equalsIgnoreCase(provider)){
            return paypal_adapter.process_payment(total_price, currency, customer_id);
        }
        else{
            return "Enter a valid payment provider";
        }
    }
}
