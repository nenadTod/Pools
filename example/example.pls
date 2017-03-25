global $threshold

salience -5
no-loop
rule "Lower prices for essentials"
    when
        $essential: Product ( category.name == "Osnovno" or contains "s" and name != "Hle"+"b")
    then
        print($essential.category.name, $essential.name)
        $essential.price -= $essential.price*0.1
        print('New price: ')
        print($essential.price)
end

rule "Raise prices to threshold"
    when
        $prod: Product (price < $threshold - 10 or name > 5)
    then
        $prod.price += 5
end



