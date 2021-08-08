library(shiny)
runExample("01_hello")
runExample("04_mpg")

shinyUI(pageWithSidebar(
  headerPanel("Shiny Text"),
  sidebarPanel(
    selectInput("dataset", "Choose a dataset:", 
                choices = c("rock", "pressure", "cars")),
    
    numericInput("obs", "Number of observations to view:", 10)
  ),
  mainPanel(
    verbatimTextOutput("summary"),
    tableOutput("view")
  )
))





