global $account
global $customerBalance
global $someonesAccount

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
      $account : Account( balance > 30, account_number contains "00")
      $customer : Customer( not (last_name ( contains "y" or == "Jovanovic") or not (!="mahab" and !="Kokoda") and $customerBalance > 30) or first_name == $customerBalance)
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
      $someonesAccount.deposit(350.0)
end
