package project_cinema.java_services.configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.paypal.base.rest.APIContext;

@Configuration
public class PayPalConfig {
    
    @Value("${paypal.client.id}")
    private String client_id;

    @Value("${paypal.client.secret}")
    private String client_secret;

    @Value("${paypal.mode}")
    private String mode;

    @Bean
    public APIContext api_context(){
        APIContext context = new APIContext(client_id, client_secret, mode);
        return context;
    }
}
