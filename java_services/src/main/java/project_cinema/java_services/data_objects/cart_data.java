package project_cinema.java_services.data_objects;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "cart")
public class cart_data {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    public Integer cart_id;
    public Integer customer_id;

    public cart_data(){

    }

    public Integer getcart_id(){
        return cart_id;
    }

    public Integer getcustomer_id(){
        return customer_id;
    }

}
