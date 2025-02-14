package project_cinema.java_services.services;

import org.springframework.stereotype.Service;

/**
 * This class is responsible for managing the logic of the payment adapter
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
public interface payment_adapter {

    /**
     * This method allows to process the payment
     */
    String process_payment(Float total_price, String currency, Integer customer_id);

}
