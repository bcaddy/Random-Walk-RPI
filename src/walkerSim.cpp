#include <limits.h>

#include "walkerSim.h"

// =============================================================================
void walkerSim::seedReceptors()
{
    size_t const gridDimSqr = _gridDim * _gridDim;

    size_t counter = 0;
    while (counter < numReceptors)
    {
        size_t location = _randInt(gridDimSqr);
        if (_receptorGrid1D[location])
        {
            // This point has already been assigned. Pass
            ;
        }
        else
        {
            _receptorGrid1D[location] = true;
            counter++;
        }
    }

    for (size_t i = 0; i < _gridDim; i++)
    {
        for (size_t j = 0; j < _gridDim; j++)
        {
            std::vector<int> coords{static_cast<int>(i),static_cast<int>(j)};
            receptorGrid[i][j] = _receptorGrid1D[_coordsToIndex(coords)];
        }

    }

}
// =============================================================================

// =============================================================================
void walkerSim::runWalkers(size_t const &numWalkers,
                           size_t const &numSteps,
                           std::vector<std::vector<std::vector<int>>> &walkerPaths,
                           size_t const &ompNumThreads)
{
    // Does the actual random walk simulation.

    // Setup step options
    std::vector<std::vector<int>> const choices = {{1,0},{0,1},{0,-1},{-1,0}};
    size_t const choiceMax = choices.size()-1;
    int halfDim = static_cast<int>(_gridDim) / 2;

    // #pragma omp parallel num_threads(ompNumThreads)
    {
        for (size_t walker = 0; walker < numWalkers; walker++)
        {
            // Initialize path array
            std::vector<std::vector<int>>
            path{numSteps+1, std::vector<int>(2,INT_MIN)};

            path[0] = {halfDim,halfDim};

            size_t i=1;
            while (i < numSteps)
            {
                // Choose the step
                std::vector<int> step = choices[_randInt(choiceMax)];

                // Compute the new position
                path[i][0] = path[i-1][0] + step[0];
                path[i][1] = path[i-1][1] + step[1];

                // Check if that position has a portal
                size_t index = _coordsToIndex(path[i]);
                // #pragma omp critical (receptorAccess)
                {
                    if (_receptorGrid1D[index])
                    {
                        _receptorGrid1D[index] = false;
                        i = numSteps + 1;
                    }
                }
                // Increment index
                i++;
            }
            // Save the path
            walkerPaths[walker] = path;
        }
    }
}
// =============================================================================

// =============================================================================
walkerSim::walkerSim(size_t const &gridLen,
                     double const &mu)
    : _gridDim(gridLen),
      _receptorGrid1D(_gridDim*_gridDim, false),
      _mu(mu),
      receptorGrid(_gridDim, std::vector<bool>(_gridDim, false)),
      numReceptors(std::floor(_randNormal(0.05 * _gridDim * _gridDim, _mu)))
{
    // Initialize the grid of receptors
}

walkerSim::~walkerSim()
{
}
// =============================================================================