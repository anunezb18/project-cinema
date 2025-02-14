package project_cinema.java_services.data_objects;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * This class is responsible for managing the data of the orders entity 
 * from the database.
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
@Entity
@Table(name = "orders")
public class order_data {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="order_id")
    public Integer id;
    public Integer customer_id;
    public Float total_price;   
    public LocalDateTime order_date;

    /**
     * This method allows to create an order object
     */
    public order_data(Integer customer_id, Float total_price) {
        this.customer_id = customer_id;
        this.total_price = total_price;
        this.order_date = LocalDateTime.now();
    }

    /**
     * This method allows to create an order object without parameters
     */ 
    public order_data(){
    }

    /**
     * This method allows to get the order id
     */
    public Integer getId() {
        return id;
    }

    /**
     * This method allows to get the customer id
     */
    public Integer getCustomer_id() {
        return customer_id;
    }

    /**
     * This method allows to get the total price
     */
    public Float getTotal_price() {
        return total_price;
    }

    /**
     * This method allows to set the total price
     */
    public void setTotal_price(Float total_price) {
        this.total_price = total_price;
    }

    /**
     * This method allows to get the order date
     */
    public LocalDateTime getOrder_date() {
        return order_date;
    }

    /**
     * This method allows to set the order date
     */
    public void setOrder_date(LocalDateTime order_date) {
        this.order_date = order_date;
    }
}
