package project_cinema.java_services.controllers;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import project_cinema.java_services.services.payment_services;

/**
 * This class is responsible for managing the web services of the payment class.
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
@RestController
@RequestMapping("/payment/")
public class payment{   

    /**
     * This method allows to inject the payment services
     */
    @Autowired
    private payment_services payment_services;


    /**
     * This method allows to obtain the total price of the order by the customer id
     */
    public Optional<Float> getTotalPricebyCustomerId(@PathVariable("customer_id") Integer customer_id){
        return payment_services.getTotalPricebyCustomerId(customer_id);
    }

    /**
     * This method allows to process the payment
     */
    @PostMapping("/process")
    public String process_payment(@RequestParam String provider, @RequestParam Integer customer_id, String currency){
        return payment_services.process_payment(provider, customer_id, currency);
    }
}
