global $accountService
global $customerBalance

salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : Account( balance < 100.46 )
    then
      $account.balance = 10000000
end

no-loop
rule "accountBalanceAtLeast"
    when
      Account( balance < 100, type == 4)
      $customer : Customer( (accounts (>= 20 and <= 40) or (!="mahab" and !="Kokoda") and surname < 30) and mahab == 40)
    then
      print $account.balance
      $account.balance = 176
      $account.calculate()

end

rule "accLeast"
    when
      $account : Account( balance < 100)
    then
      print $account.balance
end
