package project_cinema.java_services.data_objects;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

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

    public order_data(Integer customer_id, Float total_price) {
        this.customer_id = customer_id;
        this.total_price = total_price;
        this.order_date = LocalDateTime.now();
    }

    public order_data(){
    }

    public Integer getId() {
        return id;
    }

    public Integer getCustomer_id() {
        return customer_id;
    }

    public Float getTotal_price() {
        return total_price;
    }

    public void setTotal_price(Float total_price) {
        this.total_price = total_price;
    }

    public LocalDateTime getOrder_date() {
        return order_date;
    }

    public void setOrder_date(LocalDateTime order_date) {
        this.order_date = order_date;
    }
}
