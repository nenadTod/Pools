global $account
global $customerBalance
global $someonesAccount

salience 10
rule "studentWithLowAccountBalance"
    when
       $account : Account( balance < 500.46 + balance )
    then
      $account.balance = 1000
      $account.withdraw(300.0)
end


salience 15
no-loop
rule "accountBalanceAtLeast"
    when
      $account : Account( balance > 30 + 2 * 100, account_number contains "00")
      $customer : Customer( last_name ( contains first_name or != "Petrovic") and not (=="Milovanovic" or =="Markovic") and account.balance > $customerBalance and $someonesAccount.account_number == "004")
    then
      print($customer.first_name)
      print ($account.balance)
      $account.balance = 176
      $account.deposit(400)

end


rule "accLeast"
    when
      $account : Account( balance > 100)
    then
      $account.balance = 100000
      print ($account.balance)
end


rule "checkNested"
    when
        $customer :  Customer( account.balance < 50 + 100 * 2 or >= 10000 and first_name contains "Jova")
    then
        print("Account number of customer "+$customer.first_name+" "+$customer.last_name+" is: "+$customer.account.account_number)
end