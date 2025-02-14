package project_cinema.java_services.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import jakarta.transaction.Transactional;
import project_cinema.java_services.data_objects.order_data;

/** 
 * This module contains some implementations of the order class into the database.
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
@Repository
public interface payment_repository extends JpaRepository<order_data, Integer> {
    
    /**
     * This method allows to obtain the total price of the order by the customer id
     */
    @Query(value = "SELECT total_price FROM orders WHERE customer_id = ?", nativeQuery = true)
    public Optional<Float> getTotalPricebyCustomerId(Integer customer_id);

    /**
     * This method allows to delete the order by the customer id
     */
    @Modifying
    @Transactional
    @Query(value = "DELETE FROM orders WHERE customer_id = ?", nativeQuery = true)
    public void deletOrderByCustomerId(Integer customer_id);
}
