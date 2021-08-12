function ok(callback){
	let b=10;
	let x=8;
	let c=x*b;
	callback(c);
}
ok((c)=>{console.log(c)});