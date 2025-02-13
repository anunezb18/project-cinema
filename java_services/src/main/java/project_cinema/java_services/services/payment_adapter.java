package project_cinema.java_services.services;

import org.springframework.stereotype.Service;

@Service
public interface payment_adapter {

    String process_payment(Float total_price, String currency, Integer customer_id);

}
