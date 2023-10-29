import org.testng.Assert;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

public class CaracteresFrasesTest {
    CaracteresFrases cf;

    @BeforeSuite
    public void setUp() {
        cf = new CaracteresFrases();
        System.out.println("Instanciar clase CaracteresFrases");
    }

    @Test(testName = "Frase menor que n*2 caracteres", priority = 0)
    public void fraseMenor() {
        try{
            cf.caracteres(3,"hola");
            Assert.fail("El método no devolvió una excepción");
        }
        catch(Exception e){

        }
    }

    @Test(testName = "Frase igual a n*2 caracteres", priority = 0)
    public void fraseIgual() {
        try{
            cf.caracteres(2,"hola");
            Assert.fail("El método no devolvió una excepción");
        }
        catch(Exception e){

        }
    }

    @Test(testName = "Frase nula", priority = 0)
    public void fraseNula() {
        try{
            cf.caracteres(2,null);
            Assert.fail("El método no devolvió una excepción");
        }
        catch(Exception e){

        }
    }

    @Test(testName = "Frase mayor a n*2 caracteres", priority = 0)
    public void fraseMayor() {
        Assert.assertEquals(cf.caracteres(2,"hola mundo"),"ho do");
    }
}
