global $accountService
global $customerBalance

salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : Account( acc_balance < 100.46 )
    then
      $account.accBalance = 1000
      $account.withdrawal(300.0)
end

no-loop
rule "accountBalanceAtLeast"
    when
      Account( acc_balance < 500, accountNumber == "003")
      $customer : Customer( not (first_name (== "Marko" or == "Jovan") or not (!="mahab" and !="Kokoda") and $customerBalance < 30) and last_name == $customerBalance)
    then
      print $account.balance
      $account.accBalance = 176
      $account.deposit(400)

end

rule "accLeast"
    when
      $account : Account( acc_balance < 100)
    then
      print $account.accBalance
end
