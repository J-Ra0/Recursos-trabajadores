#let render-problem(
  name: "",
  author: (),
  time_limit: "",
  memory_limit: "",
  statement: [],
  input: [],
  output: [],
  sample_input: "",
  sample_output: "",
  explanation: [],
) = block[
  //#set page(margin: 2.5cm)

  #align(center)[
    #text(size: 24pt, weight: "bold")[#name]
  ]
  
  #align(center)[    
    Límite de tiempo: #time_limit • Límite de memoria: #memory_limit
  ]

  #box(height: 0.3cm)[]

  #statement

  #heading[Entrada]
  #input

  #heading[Salida]
  #output

  #heading[Ejemplo de Entrada]
  #block(
    width: 16cm,
    inset: 8pt,
    stroke: 1pt,
    [#text(font: "monospace")[#sample_input]]
  )

  #heading[Ejemplo de Salida]
  #block(
    width: 16cm,
    inset: 8pt,
    stroke: 1pt,
    [#text(font: "monospace")[#sample_output]]
  )

  #if explanation != "" [
    #heading[Explicación]
    #explanation
  ]

  #if author.len() != 0 [
    #heading[Autores]
    #for elemento in author [
      - #elemento
    ]
  ]

  //#box(height: 2cm)[]
  #align(center)[
    _Ra0 course_
  ]
]
