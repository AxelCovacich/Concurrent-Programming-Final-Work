package src;

import java.util.concurrent.Semaphore;


public class Monitor {

    private RdP RP;
    public Semaphore mutex;
    private Politicas politica;
    private Colas colas;

    public Monitor(RdP red, Politicas politica,Colas colas){
        this.politica = politica;
        RP = red;
        this.colas = colas;
        mutex = new Semaphore(1,true);
    }

    public void Disparar (int [][] secuencia) {

        boolean disparar = false;

        

            try {
                mutex.acquire();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                return;
            }


            disparar = RP.dispararTransicion(secuencia); // intentamos disparar

            // si no puede disparar entonces
            while (!disparar){
                if(RP.getDormirse() && RP.esTemporal(secuencia)) {
                    RP.setDormirse(false);    //bajo el flag, borro el indicador para el proximo hilo

                    try{
                        // suelta el mutex ya que debe dormirse
                        mutex.release();
                        Thread.sleep(RP.getSleepTime());
                    }
                    catch (InterruptedException exception){
                        exception.printStackTrace();
                        Thread.currentThread().interrupt();
                        return;
                    }
                    try {
                        // una vez que se levanta debe intentar adquirir el monitor de nuevo
                        mutex.acquire();
                    }
                    catch (InterruptedException exception){
                        exception.printStackTrace();
                        Thread.currentThread().interrupt();
                        return;
                    }
                }
                else {
                    mutex.release();
                    colas.setDormirse(secuencia);
                }
                // cuando se despierte va a volver a preguntar si puede disparar
                disparar = RP.dispararTransicion(secuencia);
            }


            /* Ya disparo, busca a quien despertar */
            Log.Tlogger(secuencia);


            int[][] sensAndDormidos = Utils.calcularAND(RP.getSensibilizado(),colas.getDormidos());
            int cantDormidosSens = 0;

            for (int[] sensibilizada : sensAndDormidos) {
                if (sensibilizada[0] == 1) {
                    cantDormidosSens++;
                }
            }

            // si hay uno o mas hilos dormidos cuya transicion esta sensibilizada debemos despertar uno
            if(cantDormidosSens > 0) {
                int indexTransicion = politica.decideTransicion(cantDormidosSens,sensAndDormidos);
                colas.signal(indexTransicion);
                return;
            }

            /* Soltamos el mutex en caso de no haber nadie esperando en alguna transicion. Entra un hilo en la cola del monitor. */
            mutex.release();

    

    }
}

