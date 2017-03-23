global $accountService
global $customerBalance

salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : Account( acc_balance < 100.46 )
    then
      $account.acc_balance = 1000
      $account.withdraw(300.0)
end

no-loop

rule "accountBalanceAtLeast"
    when
      $account : Account( acc_balance < 600, account_number == "003")
      $customer : Customer( not (first_name (== "Marko" or == "Jovan") or not (!="mahab" and !="Kokoda") and $customerBalance > 30) or last_name == $customerBalance)
    then
      print ($account.acc_balance)
      $account.acc_balance = 176
      $account.deposit(400)

end

rule "accLeast"
    when
      $account : Account( acc_balance < 100)
    then
      print ($account.acc_balance)
end
