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

/**
 * This class is responsible for managing the logic of the PayPal adapter
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
public class paypal_adapter implements payment_adapter{
    
    @Autowired
    private APIContext apiContext;


    @Autowired
    private payment_repository payment_repository;

    /**
     * This method allows to process the payment with the paypal API
     */
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
