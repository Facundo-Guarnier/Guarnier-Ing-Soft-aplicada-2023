public class CaracteresFrases {
    public String caracteres(int n, String frase) {
        
        if (frase == null || frase.length() <= n * 2) {
            throw new IllegalArgumentException("La frase debe tener al menos 2*n caracteres y no ser nula."); 
        }
        String principio = frase.substring(0, n);
        
        String finalFrase = frase.substring(frase.length() - n);
        
        return principio + " " + finalFrase;
    }
}
