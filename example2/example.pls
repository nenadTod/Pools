global $account
global $customerBalance

salience 10
rule "studentWithLowAccountBalance"
    when
       $account : Account( balance < 500.46 )
    then
      $account.balance = 1000
      $account.withdraw(300.0)
end

no-loop
rule "accountBalanceAtLeast"
    when
      $account : Account( balance < 600, account_number == "003")
      $customer : Customer( not (first_name (== "Marko" or == "Jovan") or not (!="mahab" and !="Kokoda") and $customerBalance > 30) or last_name == $customerBalance)
    then
      print ($account.balance)
      $account.balance = 176
      $account.deposit(400)

end

rule "accLeast"
    when
      $account : Account( balance > 100)
    then
      print ($account.balance)
end
