//------------------------------------------------------------------------------
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include "EPOSControl/include/EPOSControl/EPOSControl.h"

//------------------------------------------------------------------------------
#if !defined(WIN32) || defined(__CYGWIN__)
void catchSignal( int sig )
{
    signal( SIGTERM, catchSignal );
    signal( SIGINT, catchSignal );
    printf( "Got Signal %d\n",sig );
}
#endif

//------------------------------------------------------------------------------
int main()
{
#if !defined(WIN32) || defined(__CYGWIN__)
    // Comunicação
    signal( SIGTERM, catchSignal );
    signal( SIGINT, catchSignal );
#endif
    
    // Inicia a Biblioteca
    EPOS_InitLibrary()
    
    CANChannel* pChannel = EPOS_OpenCANChannel( "libCanUSBDriver.so", "32", eBR_1M );


    // Aguarda
    pause();
    
    // Finaliza a Biblioteca
    EPOS_CloseCANChannel( pChannel );
    EPOS_DeinitLibrary();
    
    return 0;
}
