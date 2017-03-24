global $account
global $customerBalance
global $someonesAccount

rule "checkNested"
    when
        $customer :  Customer( account.balance < 500.46 )
    then
        print($customer.account.account_number + "yeayea")
end