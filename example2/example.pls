global $accountService
global $customerBalance

salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : not Account( balance < 100.46 )
    then
      $account.accBalance = 1000
      $account.withdrawal(300.0)
end

no-loop
rule "accountBalanceAtLeast"
    when
      $account : Account( balance < 100, type == 4)
      $customer : Customer( (accounts (>= 20 and <= 40) or (!="mahab" and !="Kokoda") and surname < 30) and mahab == 40)
    then
      print $account.balance
      $account.accBalance = 176
      $account.deposit(400)

end

rule "accLeast"
    when
      $account : Account( balance < 100)
    then
      print $account.accBalance
end
