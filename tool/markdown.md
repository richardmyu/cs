# markdown

## 1. 流程图 -- mermaid

> [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)
> [mermaid (blog)](https://mermaid-js.github.io/mermaid/#/)

### 1.0.basic

- **方向**

```
graph [TB|BT|LR|RL|TD]
```

纵向：TB：从上至下；BT：从下至上；TD：从上至下
横向：LR：从左至右；RL：从右至左

- **定义框体**

```mermaid
graph TD
    id1[带文本的矩形]
    id2(带文本的圆角矩形)
    id3>带文本的不对称的矩形]
    id4{带文本的菱形}
    id5((带文本的圆形))
```

- **定义连接线和子图**

连接线结构：

```
id1【连接【文本】符】id2
```

子图结构：

```
subgraph 子图名
子图内容
end
```

```mermaid
graph TB
  subgraph 实线
      A0[A] --- B0[B]
      A1[A] --> B1[B]
      A2[A] -- 描述 --> B2[B]
    end
    subgraph 虚线
      A3[A] -.- B3[B]
         A4[A] -.-> B4[B]
         A5[A] -. 描述 .-> B5[B]
    end
    subgraph 加粗线
      A6[A] === B6[B]
      A7[A] ==> B7[B]
      A8[A] == 描述 ==> B8[B]
    end
```

### 1.1.Flowchart

```mermaid
flowchart LR

A[Hard] -->|Text| B(Round)
B --> C{Decision}
C -->|One| D[Result 1]
C -->|Two| E[Result 2]
```

### 1.2.Sequence diagram

```mermaid
sequenceDiagram
Alice->>John: Hello John, how are you?
loop Healthcheck
    John->>John: Fight against hypochondria
end
Note right of John: Rational thoughts!
John-->>Alice: Great!
John->>Bob: How about you?
Bob-->>John: Jolly good!
```

### 1.3.Gantt chart

```mermaid
gantt
    section Section
    Completed :done,    des1, 2014-01-06,2014-01-08
    Active        :active,  des2, 2014-01-07, 3d
    Parallel 1   :         des3, after des1, 1d
    Parallel 2   :         des4, after des1, 1d
    Parallel 3   :         des5, after des3, 1d
    Parallel 4   :         des6, after des4, 1d
```

### 1.4.Class diagram

```mermaid
classDiagram
Class01 <|-- AveryLongClass : Cool
<<Interface>> Class01
Class09 --> C2 : Where am I?
Class09 --* C3
Class09 --|> Class07
Class07 : equals()
Class07 : Object[] elementData
Class01 : size()
Class01 : int chimp
Class01 : int gorilla
class Class10 {
  <<service>>
  int id
  size()
}
```

### 1.5.State diagram

```mermaid
stateDiagram-v2
[*] --> Still
Still --> [*]
Still --> Moving
Moving --> Still
Moving --> Crash
Crash --> [*]
```

### 1.6.Pie chart

```mermaid
pie
"Dogs" : 386
"Cats" : 85.9
"Rats" : 15
```

### 1.7.User Journey diagram

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 3: Me
```

### 1.8.C4 diagram

```mermaid
C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")
```

### 1.9.Git graph [experimenta]

```mermaid
gitGraph
      commit
      commit
      branch develop
      checkout develop
      commit
      commit
      checkout main
      merge develop
      commit
      commit
```
