(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[47893,54657,92509,89461],{47893:function(e,t,n){"use strict";var a=n(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var s=a(n(87041));t.default=s.default},96412:function(e){"use strict";function t(e){!function(e){var t=e.util.clone(e.languages.javascript),n=/(?:\s|\/\/.*(?!.)|\/\*(?:[^*]|\*(?!\/))\*\/)/.source,a=/(?:\{(?:\{(?:\{[^{}]*\}|[^{}])*\}|[^{}])*\})/.source,s=/(?:\{<S>*\.{3}(?:[^{}]|<BRACES>)*\})/.source;function r(e,t){return RegExp(e=e.replace(/<S>/g,function(){return n}).replace(/<BRACES>/g,function(){return a}).replace(/<SPREAD>/g,function(){return s}),t)}s=r(s).source,e.languages.jsx=e.languages.extend("markup",t),e.languages.jsx.tag.pattern=r(/<\/?(?:[\w.:-]+(?:<S>+(?:[\w.:$-]+(?:=(?:"(?:\\[\s\S]|[^\\"])*"|'(?:\\[\s\S]|[^\\'])*'|[^\s{'"/>=]+|<BRACES>))?|<SPREAD>))*<S>*\/?)?>/.source),e.languages.jsx.tag.inside.tag.pattern=/^<\/?[^\s>\/]*/,e.languages.jsx.tag.inside["attr-value"].pattern=/=(?!\{)(?:"(?:\\[\s\S]|[^\\"])*"|'(?:\\[\s\S]|[^\\'])*'|[^\s'">]+)/,e.languages.jsx.tag.inside.tag.inside["class-name"]=/^[A-Z]\w*(?:\.[A-Z]\w*)*$/,e.languages.jsx.tag.inside.comment=t.comment,e.languages.insertBefore("inside","attr-name",{spread:{pattern:r(/<SPREAD>/.source),inside:e.languages.jsx}},e.languages.jsx.tag),e.languages.insertBefore("inside","special-attr",{script:{pattern:r(/=<BRACES>/.source),alias:"language-javascript",inside:{"script-punctuation":{pattern:/^=(?=\{)/,alias:"punctuation"},rest:e.languages.jsx}}},e.languages.jsx.tag);var i=function(e){return e?"string"==typeof e?e:"string"==typeof e.content?e.content:e.content.map(i).join(""):""},o=function(t){for(var n=[],a=0;a<t.length;a++){var s=t[a],r=!1;if("string"!=typeof s&&("tag"===s.type&&s.content[0]&&"tag"===s.content[0].type?"</"===s.content[0].content[0].content?n.length>0&&n[n.length-1].tagName===i(s.content[0].content[1])&&n.pop():"/>"===s.content[s.content.length-1].content||n.push({tagName:i(s.content[0].content[1]),openedBraces:0}):n.length>0&&"punctuation"===s.type&&"{"===s.content?n[n.length-1].openedBraces++:n.length>0&&n[n.length-1].openedBraces>0&&"punctuation"===s.type&&"}"===s.content?n[n.length-1].openedBraces--:r=!0),(r||"string"==typeof s)&&n.length>0&&0===n[n.length-1].openedBraces){var u=i(s);a<t.length-1&&("string"==typeof t[a+1]||"plain-text"===t[a+1].type)&&(u+=i(t[a+1]),t.splice(a+1,1)),a>0&&("string"==typeof t[a-1]||"plain-text"===t[a-1].type)&&(u=i(t[a-1])+u,t.splice(a-1,1),a--),t[a]=new e.Token("plain-text",u,null,u)}s.content&&"string"!=typeof s.content&&o(s.content)}};e.hooks.add("after-tokenize",function(e){("jsx"===e.language||"tsx"===e.language)&&o(e.tokens)})}(e)}e.exports=t,t.displayName="jsx",t.aliases=[]},87041:function(e,t,n){"use strict";var a=n(96412),s=n(4979);function r(e){var t,n;e.register(a),e.register(s),t=e.util.clone(e.languages.typescript),e.languages.tsx=e.languages.extend("jsx",t),delete e.languages.tsx.parameter,delete e.languages.tsx["literal-property"],(n=e.languages.tsx.tag).pattern=RegExp(/(^|[^\w$]|(?=<\/))/.source+"(?:"+n.pattern.source+")",n.pattern.flags),n.lookbehind=!0}e.exports=r,r.displayName="tsx",r.aliases=[]},4979:function(e){"use strict";function t(e){var t;e.languages.typescript=e.languages.extend("javascript",{"class-name":{pattern:/(\b(?:class|extends|implements|instanceof|interface|new|type)\s+)(?!keyof\b)(?!\s)[_$a-zA-Z\xA0-\uFFFF](?:(?!\s)[$\w\xA0-\uFFFF])*(?:\s*<(?:[^<>]|<(?:[^<>]|<[^<>]*>)*>)*>)?/,lookbehind:!0,greedy:!0,inside:null},builtin:/\b(?:Array|Function|Promise|any|boolean|console|never|number|string|symbol|unknown)\b/}),e.languages.typescript.keyword.push(/\b(?:abstract|declare|is|keyof|readonly|require)\b/,/\b(?:asserts|infer|interface|module|namespace|type)\b(?=\s*(?:[{_$a-zA-Z\xA0-\uFFFF]|$))/,/\btype\b(?=\s*(?:[\{*]|$))/),delete e.languages.typescript.parameter,delete e.languages.typescript["literal-property"],t=e.languages.extend("typescript",{}),delete t["class-name"],e.languages.typescript["class-name"].inside=t,e.languages.insertBefore("typescript","function",{decorator:{pattern:/@[$\w\xA0-\uFFFF]+/,inside:{at:{pattern:/^@/,alias:"operator"},function:/^[\s\S]+/}},"generic-function":{pattern:/#?(?!\s)[_$a-zA-Z\xA0-\uFFFF](?:(?!\s)[$\w\xA0-\uFFFF])*\s*<(?:[^<>]|<(?:[^<>]|<[^<>]*>)*>)*>(?=\s*\()/,greedy:!0,inside:{function:/^#?(?!\s)[_$a-zA-Z\xA0-\uFFFF](?:(?!\s)[$\w\xA0-\uFFFF])*/,generic:{pattern:/<[\s\S]+/,alias:"class-name",inside:t}}}}),e.languages.ts=e.languages.typescript}e.exports=t,t.displayName="typescript",t.aliases=["ts"]},64836:function(e){e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports}}]);