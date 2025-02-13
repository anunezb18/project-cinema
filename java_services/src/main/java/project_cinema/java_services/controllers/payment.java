package project_cinema.java_services.controllers;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import project_cinema.java_services.services.payment_services;

@RestController
@RequestMapping("/payment/")
public class payment{   

    @Autowired
    private payment_services payment_services;


    public Optional<Float> getTotalPricebyCustomerId(@PathVariable("customer_id") Integer customer_id){
        return payment_services.getTotalPricebyCustomerId(customer_id);
    }

    @PostMapping("/process")
    public String process_payment(@RequestParam String provider, @RequestParam Integer customer_id, String currency){
        return payment_services.process_payment(provider, customer_id, currency);
    }
}
