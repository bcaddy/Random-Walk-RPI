/*!
 * \file walkerSim.h
 * \author Robert 'Bob' Caddy (rvc@pitt.edu)
 * \brief Header for class to perform random walk
 * \version 0.1
 * \date 2021-07-13
 *
 * \copyright Copyright (c) 2021
 *
 */

#pragma once

#include <random>
#include <cmath>
#include <omp.h>

#include "utility.h"

/*!
 * \brief Class to perform a random walk
 *
 */
class walkerSim
{
private:
    /// The size of the grid in each dimension. Currently requires a square
    /// board though that could be easily changed
    size_t const _gridDim;

    /// The grid of receptor positions
    std::vector<bool> _receptorGrid1D;

    /// The Chemical Potential/standard deviation of the Gaussian used
    double const _mu;

    // =========================================================================
    // Random number generators
    // =========================================================================
    inline int _randInt(int const &max)
    {
        static thread_local std::random_device rd;
        static thread_local std::mt19937_64 generator(rd()+omp_get_thread_num());
        std::uniform_int_distribution<int> distribution(0,max);
        return distribution(generator);
    }
    inline double _randNormal(double const &mean,
                       double const &stdDev)
    {
        static thread_local std::random_device rd;
        static thread_local std::mt19937_64 generator(rd()+omp_get_thread_num());
        std::normal_distribution<double> distribution(mean, stdDev);
        return distribution(generator);
    }
    inline int _randFlat(double const &min,
                  double const &max)
    {
        static thread_local std::random_device rd;
        static thread_local std::mt19937_64 generator(rd()+omp_get_thread_num());
        std::uniform_real_distribution<double> distribution(min,max);
        return distribution(generator);
    }
    // =========================================================================
    // End Random number generators
    // =========================================================================

    /// Perform the random walk for one walker
    std::vector<std::vector<size_t>> _runWalker(size_t const &numSteps);

    /// This function converts the coordinate system to a list index
    /// There is an intermediate transformation into a matrix like coordinate
    inline size_t _coordsToIndex(std::vector<int> const &coord)
    {return coord[0] + _gridDim * coord[1];}

public:
    /// The grid of receptor positions
    std::vector<std::vector<bool>> receptorGrid;

    /// The number of receptors
    size_t const numReceptors;

    /// Seed the location of the receptors
    void seedReceptors();

    /// Perform the walk
    void runWalkers(size_t const &numWalkers,
                    size_t const &numSteps,
                    std::vector<std::vector<std::vector<int>>> &walkerPaths,
                    size_t const &ompNumThreads);

    /// Constructor and Destructor
    walkerSim(size_t const &gridLen,
              double const &mu);
    ~walkerSim();
};
