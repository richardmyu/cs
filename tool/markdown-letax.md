# markdown 中常用 LaTex

## 1.通用符号

| 符号         | 代码           |
| ------------ | -------------- |
| $\{$         | `$\{$`         |
| $\}$         | `$\}$`         |
| $\$$         | `$\$$`         |
| $\%$         | `$\%$`         |
| $\dag$       | `$\dag$`       |
| $\S$         | `$\S$`         |
| $\copyright$ | `$\copyright$` |
| $\dots$      | `$\dots$`      |
| $\ddag$      | `$\ddag$`      |
| $\P$         | `$\P$`         |
| $\pounds$    | `$\pounds$`    |

## 2.希腊字母

`\Alpha`、`\Beta` 等希腊字母符号不存在，因为它们和拉丁字母 A、B 等一模一样；小写字母里也不存在 `\omicron`，直接用拉丁字母 `o` 替代。

大写希腊字母一般是正体，带有 `\var` 命令的则是斜体样式，需要在导言区加载 amsmath 宏包。

| 符号        | 代码          | 符号        | 代码          | 符号          | 代码            |
| ----------- | ------------- | ----------- | ------------- | ------------- | --------------- |
| $\alpha$    | `$\alpha$`    | $\beta$     | `$\beta$`     | $\gamma$      | `$\gamma$`      |
| $\delta$    | `$\delta$`    | $\epsilon$  | `$\epsilon$`  | $\varepsilon$ | `$\varepsilon$` |
| $\zeta$     | `$\zeta$`     | $\eta$      | `$\eta$`      | $\theta$      | `$\theta$`      |
| $\vartheta$ | `$\vartheta$` | $\iota$     | `$\iota$`     | $\kappa$      | `$\kappa$`      |
| $\lambda$   | `$\lambda$`   | $\mu$       | `$\mu$`       | $\nu$         | `$\nu$`         |
| $\xi$       | `$\xi$`       | $o$         | `$o$`         | $\pi$         | `$\pi$`         |
| $\varpi$    | `$\varpi$`    | $\rho$      | `$\rho$`      | $\varrho$     | `$\varrho$`     |
| $\sigma$    | `$\sigma$`    | $\varsigma$ | `$\varsigma$` | $\tau$        | `$\tau$`        |
| $\upsilon$  | `$\upsilon$`  | $\phi$      | `$\phi$`      | $\varphi$     | `$\varphi$`     |
| $\chi$      | `$\chi$`      | $\psi$      | `$\psi$`      | $\omega$      | `$\omega$`      |

| 符号       | 代码         | 符号          | 代码            |
| ---------- | ------------ | ------------- | --------------- |
| $\Gamma$   | `$\Gamma$`   | $\varGamma$   | `$\varGamma$`   |
| $\Delta$   | `$\Delta$`   | $\varDelta$   | `$\varDelta$`   |
| $\Theta$   | `$\Theta$`   | $\varTheta$   | `$\varTheta$`   |
| $\Lambda$  | `$\Lambda$`  | $\varLambda$  | `$\varLambda$`  |
| $\Xi$      | `$\Xi$`      | $\varXi$      | `$\varXi$`      |
| $\Pi$      | `$\Pi$`      | $\varPi$      | `$\varPi$`      |
| $\Sigma$   | `$\Sigma$`   | $\varSigma$   | `$\varSigma$`   |
| $\Upsilon$ | `$\Upsilon$` | $\varUpsilon$ | `$\varUpsilon$` |
| $\Phi$     | `$\Phi$`     | $\varPhi$     | `$\varPhi$`     |
| $\Psi$     | `$\Psi$`     | $\varPsi$     | `$\varPsi$`     |
| $\Omega$   | `$\Omega$`   | $\varOmega$   | `$\varOmega$`   |

## 3.二元关系

所有的二元关系符都可以加 `\not` 前缀得到相反意义的关系符。

| 符号          | 代码            | 符号          | 代码            | 符号         | 代码           |
| ------------- | --------------- | ------------- | --------------- | ------------ | -------------- |
| $<$           | `$<$`           | $>$           | `$>$`           | $=$          | `$=$`          |
| $\le$         | `$\leq$ $\le$`  | $\ge$         | `$\geq$ $\ge$`  | $\equiv$     | `$\equiv$`     |
| $\ll$         | `$\ll$`         | $\gg$         | `$\gg$`         | $\doteq$     | `$\doteq$`     |
| $\prec$       | `$\prec$`       | $\succ$       | `$\succ$`       | $\sim$       | `$\sim$`       |
| $preceq$      | `$preceq$`      | $succeq$      | `$succeq$`      | $\simeq$     | `$\simeq$`     |
| $subset$      | `$subset$`      | $supset$      | `$supset$`      | $\approx$    | `$\approx$`    |
| $\subseteq$   | `$\subseteq$`   | $supseteq$    | `$supseteq$`    | $\cong$      | `$\cong$`      |
| $\sqsubset$   | `$\sqsubset$`   | $\sqsupset$   | `$\sqsupset$`   | $\Join$      | `$\Join$`      |
| $\sqsubseteq$ | `$\sqsubseteq$` | $sqsupseteq$  | `$sqsupseteq$`  | $\bowtie$    | `$\bowtie$`    |
| $\in$         | `$\in$`         | $\ni$ $\owns$ | `$\ni$ $\owns$` | $\propto$    | `$\propto$`    |
| $\vdash$      | `$\vdash$`      | $\dashv$      | `$\dashv$`      | $\models$    | `$\models$`    |
| $\mid$        | `$\mid$`        | $\parallel$   | `$\parallel$`   | $perp$       | `$perp$`       |
| $\smile$      | `$\smile$`      | $\frown$      | `$\frown$`      | $\asymp$     | `$\asymp$`     |
| $:$           | `$:$`           | $\notin$      | `$\notin$`      | $\neq$ $\ne$ | `$\neq$ $\ne$` |

## 4.二元运算符

| 符号             | 代码               | 符号               | 代码                 | 符号             | 代码               |
| ---------------- | ------------------ | ------------------ | -------------------- | ---------------- | ------------------ |
| $+$              | `$+$`              | $-$                | `$-$`                | &nbsp;           | &nbsp;             |
| $\pm$            | `$\pm$`            | $\mp$              | `$\mp$`              | $\triangleleft$  | `$\triangleleft$`  |
| $\cdot$          | `$\cdot$`          | $\div$             | `$\div$`             | $\triangleright$ | `$\triangleright$` |
| $\times$         | `$\times$`         | $\setminus$        | `$\setminus$`        | $\star$          | `$\star$`          |
| $\cup$           | `$\cup$`           | $\cap$             | `$\cap$`             | $\ast$           | `$\ast$`           |
| $\sqcup$         | `$\sqcup$`         | $\sqcap$           | `$\sqcap$`           | $\circ$          | `$\circ$`          |
| $\vee$           | `$\vee$ $\lor$`    | $\wedge$           | `$\wedge$ $\land$`   | $\bullet$        | `$\bullet$`        |
| $\oplus$         | `$\oplus$`         | $\ominus$          | `$\ominus$`          | $\diamond$       | `$\diamond$`       |
| $\odot$          | `$\odot$`          | $\oslash$          | `$\oslash$`          | $\uplus$         | `$\uplus$`         |
| $\otimes$        | `$\otimes$`        | $\bigcirc$         | `$\bigcirc$`         | $\amalg$         | `$\amalg$`         |
| $\bigtriangleup$ | `$\bigtriangleup$` | $\bigtriangledown$ | `$\bigtriangledown$` | $\dagger$        | `$\dagger$`        |
| $\lhd$           | `$\lhd$`           | $\rhd$             | `$\rhd$`             | $\ddagger$       | `$\ddagger$`       |
| $\unlhd$         | `$\unlhd$`         | $\unrhd$           | `$\unrhd$`           | $\wr$            | `$\wr$`            |

## 5.巨算符

| 符号        | 代码          | 符号         | 代码           | 符号        | 代码          |
| ----------- | ------------- | ------------ | -------------- | ----------- | ------------- |
| $\sum$      | `$\sum$`      | $\bigcup$    | `$\bigcup$`    | $\bigvee$   | `$\bigvee$`   |
| $\prod$     | `$\prod$`     | $\bigcap$    | `$\bigcap$`    | $\bigwedge$ | `$\bigwedge$` |
| $\coprod$   | `$\coprod$`   | $\bigsqcup$  | `$\bigsqcup$`  | $\biguplus$ | `$\biguplus$` |
| $\int$      | `$\int$`      | $\oint$      | `$\oint$`      | $\bigodot$  | `$\bigodot$`  |
| $\bigoplus$ | `$\bigoplus$` | $\bigotimes$ | `$\bigotimes$` | &nbsp;      | &nbsp;        |
| $\iint$     | `$\iint$`     | $\iiint$     | `$\iiint$`     | $\iiiint$   | `$\iiiint$`   |
| $\idotsint$ | `$\idotsint$` | &nbsp;       | &nbsp;         | &nbsp;      | &nbsp;        |

