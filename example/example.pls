global $threshold

salience -5
no-loop
rule "Lower prices for essentials"
    when
        $essential: Product ( category.name == "Osnovno")
    then
        $essential.price -= $essential.price*0.1
        print('New price: ')
        print($essential.price)
end

rule "Raise prices to threshold"
    when
        $prod: Product (price < $threshold)
    then
        $prod.price += 5
end



