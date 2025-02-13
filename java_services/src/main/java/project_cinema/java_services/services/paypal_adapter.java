package project_cinema.java_services.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.paypal.api.payments.Amount;
import com.paypal.api.payments.Links;
import com.paypal.api.payments.Payer;
import com.paypal.api.payments.Payment;
import com.paypal.api.payments.RedirectUrls;
import com.paypal.api.payments.Transaction;
import com.paypal.base.rest.APIContext;
import com.paypal.base.rest.PayPalRESTException;

import project_cinema.java_services.repositories.payment_repository;

@Service
public class paypal_adapter implements payment_adapter{
    
    @Autowired
    private APIContext apiContext;


    @Autowired
    private payment_repository payment_repository;

    @Override
    public String process_payment(Float total_price, String currency, Integer customer_id){
        Amount amount = new Amount();
        amount.setCurrency(currency);
        amount.setTotal(String.format("%.2f", total_price));

        Transaction transaction = new Transaction();
        transaction.setAmount(amount);
        transaction.setDescription("Payment of an order of CineMacondo");

        Payer customer = new Payer();
        customer.setPaymentMethod("paypal");

        Payment payment = new Payment();
        payment.setIntent("sale");
        payment.setPayer(customer);
        payment.setTransactions(java.util.List.of(transaction));

        RedirectUrls redirect = new RedirectUrls();
        redirect.setCancelUrl("http://localhost:8001/payment/cancel");
        redirect.setReturnUrl("http://localhost:8001/payment/return");
        payment.setRedirectUrls(redirect);

        try {
            Payment created_payment = payment.create(apiContext);
            for (Links link : created_payment.getLinks()){
                if(link.getRel().equals("approval_url")){
                    payment_repository.deletOrderByCustomerId(customer_id);
                    return "Payment successfully completed, approval url: " + link.getHref();
                }
            }
        } catch (PayPalRESTException e) {
            return "Error with the payment on PayPal: " + e;
        }
        return "Error with the payment on PayPal";
    }

}
