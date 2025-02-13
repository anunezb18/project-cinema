package project_cinema.java_services.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import jakarta.transaction.Transactional;
import project_cinema.java_services.data_objects.order_data;

@Repository
public interface payment_repository extends JpaRepository<order_data, Integer> {
    
    @Query(value = "SELECT total_price FROM orders WHERE customer_id = ?", nativeQuery = true)
    public Optional<Float> getTotalPricebyCustomerId(Integer customer_id);

    @Modifying
    @Transactional
    @Query(value = "DELETE FROM orders WHERE customer_id = ?", nativeQuery = true)
    public void deletOrderByCustomerId(Integer customer_id);
}
