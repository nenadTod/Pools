global $accountService
global $customerBalance

salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : Account( balance < 100.46 )
    then
      $account.acc_balance = 1000
      $account.withdraw(300.0)
end

no-loop

rule "accountBalanceAtLeast"
    when
      Account( balance < 100, type == 4)
      $customer : Customer( not (accounts (>= 20 and <= 40) or not (!="mahab" and !="Kokoda") and $customerBalance < 30) and mahab == $customerBalance)
    then
      print ($account.acc_balance)
      $account.acc_balance = 176
      $account.deposit(400)

end

rule "accLeast"
    when
      $account : Account( balance < 100)
    then
      print ($account.acc_balance)
end
