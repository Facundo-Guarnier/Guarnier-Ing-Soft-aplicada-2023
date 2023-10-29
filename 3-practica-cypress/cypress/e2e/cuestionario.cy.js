
describe('template spec', () => {
  it('passes', () => {
    //! Inicio de sesion
    cy.visit('https://virtual.um.edu.ar/login/index.php');
    cy.get('#username').click();
    cy.get('#username').type("fj.guarnier");
    cy.get('#password').type("**********");
    cy.get('#loginbtn').click();

    //! Cuestionario
    cy.visit('https://virtual.um.edu.ar/mod/questionnaire/complete.php?id=210589')
    
    //! Pregunta 1: Si
    cy.get('#auto-rb0001').click();
    
    //! Pregunta 2:
    cy.get('#dropSelecciòn').select('4053');
    
    //! Enviar
    cy.get('.buttons > .btn').click();
    cy.url().should('contains', 'https://virtual.um.edu.ar/mod/questionnaire/complete.php');

    //! Continuar
    cy.get('.mod_questionnaire_completepage button.btn.btn-secondary').click();
    cy.url().should('contains', 'https://virtual.um.edu.ar/mod/questionnaire/myreport.php');
    
  })
})