/** 
 * This module contains the implementation of the order class into the database.
 * @Author: <anunezb@udistrital.edu.co>, <masanabriap@udistrital.edu.co>
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
package project_cinema.java_services.repositories;


import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import project_cinema.java_services.data_objects.order_data;

@Repository
public interface order_repository extends JpaRepository<order_data, Integer>{

        /**
         * 
         * This method allows to obtain every order on the database
         * 
         */
        @Query(value = "SELECT * FROM orders", nativeQuery = true)
        List<order_data> getAllOrders();

        /**
         * This method allows to obtain the order by its id
         * @param id
         * @return Order that has the asked id
         */
        @Query(value = "SELECT * FROM orders WHERE order_id = ?", nativeQuery = true)
        Optional<order_data> getOrderbyId(Integer id);

        @Query(value = """
                       SELECT SUM(price) AS total_price FROM cart 
                       INNER JOIN cart_item ON cart.cart_id = cart_item.cart_id 
                       INNER JOIN customers ON cart.customer_id = customers.customer_id 
                       INNER JOIN tickets ON cart_item.ticket_id = tickets.ticket_id
                       GROUP BY customers.customer_id
                       """, nativeQuery=true)
        Optional<Float> getTotalPricebyCustomerId(Integer customer_id);
}
    