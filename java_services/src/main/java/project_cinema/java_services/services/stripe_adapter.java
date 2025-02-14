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

/**
 * This class is responsible for managing the logic of the Stripe adapter
 * Author: <anunezb@udistrital.edu.co>, <masanabriap@udistrital.edu.co>
 * 
 * CineMacondo is free software: you can redistribute it and/or 
 * modify it under the terms of the GNU General Public License as 
 * published by the Free Software Foundation, either version 3 of 
 * the License, or (at your option) any later version.
 * 
 * CineMacondo is distributed in the hope that it will be useful, 
 * but WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License 
 * along with CineMacondo. If not, see <https://www.gnu.org/licenses/>.
 */
@Service
public class stripe_adapter implements payment_adapter{
    
    @Value("${stripe.key}")
    private String stripe_key;

    @Autowired
    private payment_repository payment_repository;

    /**
     * This method allows to process the payment with the Stripe API
     */
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
