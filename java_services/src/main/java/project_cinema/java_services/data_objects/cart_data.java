package project_cinema.java_services.data_objects;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

/**
 * This class is responsible for managing the data of the cart entity 
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
@Table(name = "cart")
public class cart_data {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    public Integer cart_id;
    public Integer customer_id;

    /**
     * This method allows to create a cart object without parameters
     */
    public cart_data(){
    }

    /**
     * This method allows get the cart id
     */
    public Integer getcart_id(){
        return cart_id;
    }

    /**
     * This method allows to get the customer id
     */
    public Integer getcustomer_id(){
        return customer_id;
    }

}
