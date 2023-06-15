//c-differential
clear;
p:=2;
for m in [3..7] do
m;
q:=p^m;
F<w>:=FiniteField(q);
F1:=[x: x in F| Trace(x) eq 1 and x ne 1];
t:=F1[1];
DF:={<x1,x2>: x1, x2 in F};
DF0:={x: x in DF|<x[1],x[2]> ne <0,0>};  
DF1:={x: x in DF|<x[1],x[2]> ne <1,0>};
DF2:={x: x in DF1| x[2] eq 0};
add:=function(x,y)
return <x[1]+y[1],x[2]+y[2]>;
end function;
Multi:=function(x,y)
return <x[1]*y[1]+x[2]*y[2]*t,x[1]*y[2]+x[2]*y[1]+x[2]*y[2]>;
end function;
f:=function(x)
return <(x[1]^2+x[1]*x[2]+F1[2]*x[2]^2)^(q-2)*(x[1]),
(x[1]^2+x[1]*x[2]+F1[3]*x[2]^2)^(q-2)*(x[2])>;
end function;
for c in DF1 do
N:={};
for a in DF do
APcN:={*add(f(add(x,a)),Multi(c,f(x))):x in DF*};
L:={add(f(add(x,a)),Multi(c,f(x))):x in DF};
for b in L do
s:=Multiplicity(APcN,b);
Include(~N,s);
end for;
end for;
printf  "\n(c,APcN)=(%o,%o)\n",c,Max(N);
end for;
end for;

// classical differental 
clear;
p:=2;
for m in [3..7] do
m;
q:=p^m;
F<w>:=FiniteField(q);
F1:=[x: x in F| Trace(x) eq 1 and x ne 1];
t:=F1[1];
DF:={<x1,x2>: x1, x2 in F};
DF0:={x: x in DF|<x[1],x[2]> ne <0,0>};
DF1:={x: x in DF|<x[1],x[2]> ne <1,0>};
DF2:={x: x in DF1| x[2] eq 0};
add:=function(x,y)
return <x[1]+y[1],x[2]+y[2]>;
end function;
Multi:=function(x,y)
return <x[1]*y[1]+x[2]*y[2]*t,x[1]*y[2]+x[2]*y[1]+x[2]*y[2]>;
end function;
f:=function(x)
return <(x[1]^2+x[1]*x[2]+F1[2]*x[2]^2)^(q-2)*(x[1]),
(x[1]^2+x[1]*x[2]+F1[3]*x[2]^2)^(q-2)*(x[2])>;
end function;
c:=<1,0>;
N:={};
for a in DF0 do
APcN:={*add(f(add(x,a)),Multi(c,f(x))):x in DF*};
L:={add(f(add(x,a)),Multi(c,f(x))):x in DF};
for b in L do
s:=Multiplicity(APcN,b);
Include(~N,s);
end for;
end for;
printf  "\n(c,APcN)=(%o,%o)\n",c,Max(N);
end for;
end for;