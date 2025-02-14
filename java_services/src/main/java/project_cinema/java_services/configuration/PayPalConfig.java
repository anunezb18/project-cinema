package project_cinema.java_services.configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.paypal.base.rest.APIContext;

/**
 * This class is responsible for managing the configuration of the PayPal API
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
@Configuration
public class PayPalConfig {
    
    /**
     * This method allows to obtain the client ID from the application.properties file
     */
    @Value("${paypal.client.id}")
    private String client_id;

    /**
     * This method allows to obtain the client secret key from the application.properties file
     */
    @Value("${paypal.client.secret}")
    private String client_secret;

    /**
     * This method allows to obtain the mode of the PayPal payment from the application.properties file
     */
    @Value("${paypal.mode}")
    private String mode;

    /**
     * This method allows to creat the API context for the PayPal API
     */
    @Bean
    public APIContext api_context(){
        APIContext context = new APIContext(client_id, client_secret, mode);
        return context;
    }
}
