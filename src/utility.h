/*!
 * \file utility.h
 * \author Robert 'Bob' Caddy (rvc@pitt.edu)
 * \brief Various utility functions and definition for this project
 * \version 0.1
 * \date 2021-06-30
 *
 * \copyright Copyright (c) 2021
 *
 */

#include <vector>
#include <fstream>
#include <stdexcept>
#include <string>

// =============================================================================
// Make definition for some common vector sizes
using stdVector1D = std::vector<double>;
using stdVector2D = std::vector<std::vector<double>>;
using stdVector3D = std::vector<std::vector<std::vector<double>>>;
// =============================================================================

/*!
 * \brief Namespace for various utility functions
 *
 */
namespace utils
{
// =============================================================================
/*!
 * \brief Save two one dimensional vectors to a csv file. Each vector is one
 * column and the header is "xPosition, yPosition"
 *
 * \param xPos The vector of x-positions
 * \param yPos The vector of y-positions
 */
void saveState(stdVector1D const &xPos,
               stdVector1D const &yPos,
               std::string savePath)
{
    // Make sure the vectors are the same size
    if (xPos.size() != yPos.size())
    {
        throw std::runtime_error("Different vector sizes in utils::saveState");
    }

    // Set header name
    const std::string header="xPosition, yPosition";

    // Open the savefile
    std::ofstream saveFile;
    saveFile.open(savePath.append("/walkerFinalPositions.csv"));
    
    // Check that the save file opened
    if (saveFile.is_open())
    {
        // write the header
        saveFile << header << std::endl;

        // write to the save file
        for (size_t i = 0;
             i < xPos.size();
             i++)
        {
            saveFile << xPos[i] << ", " << yPos[i] << std::endl;
        }
    }
    else
    {
        perror("Savefile failed to open");
        throw std::runtime_error("Exiting.");
    }

    // Close the save file
    saveFile.close();
}
// =============================================================================
}