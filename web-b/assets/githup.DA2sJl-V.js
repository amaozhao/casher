import{r as A,c as C}from"./home.BkC5lZfE.js";function I(I){return A.httpRequest({url:C.flowsList,method:"GET"},I)}function g(I){return A.httpRequest({url:C.flowsList+I+"/",method:"PUT"},I)}function E(I){return A.httpRequest({url:C.flowsList+I+"/",method:"DELETE"},I)}function Q(I){return A.httpRequest({url:C.b_templates,method:"GET"},I)}function t(I){return A.httpRequest({url:C.mplogin,method:"POST"},I)}const B="data:image/png;base64,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";export{B as _,g as a,Q as b,E as c,I as f,t as m};