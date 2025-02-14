package project_cinema.java_services.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import project_cinema.java_services.data_objects.order_data;
import project_cinema.java_services.services.order_services;

/**
 * This class is responsible for managing the web services of the order class.
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
@RequestMapping("/order")
public class order {

    @Autowired
    private order_services order_services;

    /**
     * 
     * This method allows to obtain every order on the database
     * 
     */
    @GetMapping("/getAllOrders")
    public List<order_data> getAllOrders(){
        return order_services.getAllOrders();
    }

    /**
     * This method allows to obtain the order by its id
     */
    @GetMapping("/getOrderbyId/{idOrder}")
    public Optional<order_data> getOrderbyId(@PathVariable("idOrder")Integer id){
        return order_services.getOrderbyId(id);
    }

    /**
     * This method allows to create an order
     */
    @PostMapping("/createOrder")
    public Optional<order_data> createOrder(@RequestBody order_data Order){
        return order_services.createOrder(Order);
    }

    /**
     * This method allows to obtain the cart total price by the customer id
     */
    @GetMapping("/getTotalPrice/{customer_id}")
    public Optional<Float> getTotalPricebyCustomerId(@PathVariable("customer_id") Integer customer_id){
        return order_services.getTotalPricebyCustomerId(customer_id);
    }

}
