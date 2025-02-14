package project_cinema.java_services.services;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;

import project_cinema.java_services.data_objects.order_data;
import project_cinema.java_services.repositories.order_repository;

/**
 * This class is responsible for managing the logic of the order class
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
public class order_services {
    
    @Autowired
    public order_repository order_repository;
    /**
     * This method allows to obtain every order on the database
     */
    public List<order_data> getAllOrders(){
        return order_repository.getAllOrders();
    }

    /**
     * This method allows to obtain the order by its id
     */
    public Optional<order_data> getOrderbyId(@PathVariable("idOrder")Integer id){
        if(id == null || id < 0){
            return Optional.empty();
        }
        else{
            return order_repository.getOrderbyId(id);
        }
    }

    /**
     * This method allows to create an order
     */
    public Optional<order_data> createOrder(order_data Order){
        if(Order.getCustomer_id() == null){
            return Optional.empty();
        }

        Optional<Float> total_price = getTotalPricebyCustomerId(Order.getCustomer_id());
        if(total_price.isEmpty()){
            return Optional.empty();
        }

        Order.setTotal_price(total_price.get());
        Order.setOrder_date(LocalDateTime.now());

        order_data save_order = order_repository.save(Order);
        return Optional.of(save_order);
    }

    /**
     * This method allows to obtain the total price of the order by the customer id
     */
    public Optional<Float> getTotalPricebyCustomerId(@PathVariable("customer_id") Integer customer_id){
        if(customer_id == null || customer_id < 0){
            return Optional.empty();
        }
        else{
            return order_repository.getTotalPricebyCustomerId(customer_id);
        }
    }
}
