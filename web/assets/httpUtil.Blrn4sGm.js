import{T as e,m as a,U as t,p as o,V as n,n as s}from"./index-dtTw9diQ.js";function l(l){return new Promise(((i,d)=>{e({key:"storage_key",data:"hello",success:function(){console.log("success")}}),console.log("token",a("token")),t({url:"https://test.aidep.cn/"+l.url,method:l.method||"GET",data:l.data||{},header:l.header||{"Content-Type":"application/json",Authorization:"Bearer "+a("token")},success:e=>{var a,t,l,d;i(null==e?void 0:e.data),401===e.statusCode?(o({title:(null==(a=e.data)?void 0:a.detail)||(null==(t=e.data)?void 0:t.message),icon:"none"}),n({key:"token"}),s({url:"/pages/toc/toc02Login"})):o({title:(null==(l=e.data)?void 0:l.detail)||(null==(d=e.data)?void 0:d.message),icon:"none"})},fail:e=>{d(e)}})}))}export{l as r};
