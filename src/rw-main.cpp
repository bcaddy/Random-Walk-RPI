/*!
* \file rw-main.cpp
* \author Robert 'Bob' Caddy (rvc@pitt.edu)
* \brief The main function for the random walk program
* \date 2021-06-30
*
* \copyright Copyright (c) 2021
*
*/

#include <iostream>
#include <string>
#include <omp.h>
#include <vector>
#include <limits.h>

#include "utility.h"
#include "PerfTimer.h"
#include "walkerSim.h"

using std::cout;
using std::cin;
using std::endl;

/*!
 * \brief Main function for the random walk program. Controls execution of the
 * various components and provides user output.
 *
 * \param argc Total number of command line arguments
 * \param argv Array of arguments.
 * \return int 0 if successful
 */
int main(int argc, char const *argv[])
{
    // =========================================================================
    // Settings & Inputs
    // =========================================================================
    // Declare timers and start overall timer
    PerfTimer overallTimer("Overall Timer");
    PerfTimer walkerTimer("Random Walker Timer");
    PerfTimer saveTimer("Saving Timer");
    overallTimer.startTimer();

    // Setting for simulation
    size_t const numWalkers     = 1E3;                    /// The total number of walkers to make
    size_t const numAntags      = 1E3;                    /// The total number of walker antagonists to make
    size_t const numWalkerSteps = 1E4;                    /// The number of steps that each walker should take
    size_t const numAntagSteps  = 1E4;                    /// The number of steps that each walker antagonist should take
    size_t const axisLen        = 2 * numAntagSteps + 1;  /// The range of each axis. x and y both run from 0 to `axisLen`
    double const mu             = 0.014862391;            // "Chemical Potential"

    // Program settings
    std::string savePath;        /// The path to save the output to
    int ompNumThreads=1;           /// Number of OMP threads to use

    // Declare and initialize simulation object
    walkerSim sim(axisLen, mu);

    // Declare the arrays for storing results
    std::vector<std::vector<std::vector<int>>>
        walkerPaths{numWalkers,
                    std::vector<std::vector<int>>(numWalkerSteps+1,
                    std::vector<int>(2,INT_MIN))},
        antagPaths{numAntags,
                   std::vector<std::vector<int>>(numAntagSteps+1,
                   std::vector<int>(2,INT_MIN))};

    // Gather inputs and suppress unused parameters warnings for argc and argv
    if (argc >= 2) savePath = argv[1];  /// The path to save the file to
    // if (argc == 3)
    // {
    //     ompNumThreads = std::stoi(argv[2]);
    // }
    // else
    // {
    //     ompNumThreads = omp_get_max_threads();
    // }
    // cout << "Running with " << ompNumThreads << " OpenMP threads" << endl;
    cout << "numWalkers = " << numWalkers << ", numAntags = " << numAntags << endl;
    cout << "numWalkerSteps = " << numWalkerSteps << ", numAntagSteps = " << numAntagSteps << endl;
    cout << "Total steps = " << numWalkers * numWalkerSteps + numAntags * numAntagSteps << endl << endl;
    // =========================================================================
    // End Settings & Input
    // =========================================================================

    // =========================================================================
    // Random walk
    // =========================================================================
    walkerTimer.startTimer();

    // Initialize the grid of receptors
    sim.seedReceptors();

    // Run the antagonist walkers
    sim.runWalkers(numAntags, numAntagSteps, antagPaths, ompNumThreads);

    // Run the walkers
    sim.runWalkers(numWalkers, numWalkerSteps, walkerPaths, ompNumThreads);
    walkerTimer.stopTimer();
    // =========================================================================
    // End random walk
    // =========================================================================

    // =========================================================================
    // Saving and cleanup
    // =========================================================================
    // Save the vectors to a csv file
    saveTimer.startTimer();
    utils::save2DVector(sim.receptorGrid, savePath);
    utils::save3DVector(walkerPaths, savePath, "/walkerPaths.csv");
    utils::save3DVector(antagPaths, savePath, "antagonistPaths.csv");
    saveTimer.stopTimer();

    // Overall timer stop and return timing information
    overallTimer.stopTimer();
    overallTimer.reportStats();
    walkerTimer.reportStats();
    saveTimer.reportStats();
    // =========================================================================
    // End saving and cleanup
    // =========================================================================

    return 0;
}