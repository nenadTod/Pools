
salience 10
lock-on-active
rule "studentWithLowAccountBalance"
    when
       $account : Account( //balance < 100
       )
    then
      //$account.balance = 10000000
end

no-loop
rule "accountBalanceAtLeast"
    when
      $account : Account( //balance < 100
      , //type == bleja
      )
       $customer : Customer( //accounts < $account
       or //afasf = asd as
       and //asdasfa asda
       )
    then
      //print $account.balance;
end

rule "accLeast"
    when
      $account : Account( //balance < 100
      )
    then
      //print $account.balance;
end
