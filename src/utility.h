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
#pragma once

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
inline void save3DVector(std::vector<std::vector<std::vector<int>>> const &data,
                         std::string savePath,
                         std::string const &walkerType)
{
    // Open the savefile
    std::ofstream saveFile;
    std::string fullName =  savePath.append(walkerType);
    saveFile.open(fullName);

    // Check that the save file opened
    if (saveFile.is_open())
    {
        // write the header
        for (size_t i = 0; i < data.size(); i++)
        {
            saveFile << "X" + std::to_string(i) + ", Y" + std::to_string(i) + ", ";
        }

        saveFile << std::endl;

        // write to the save file
        for (size_t i = 0;
             i < data.size();
             i++)
        {
            for (size_t j = 0; j < data[i].size(); j++)
            {
                for (size_t k = 0; k < data[i][j].size(); k++)
                {
                    saveFile << data[i][j][k] << ", ";
                }
            }
            saveFile << std::endl;
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

// =============================================================================
inline void save2DVector(std::vector<std::vector<bool>> const &data,
                         std::string savePath)
{
    // Open the savefile
    std::ofstream saveFile;
    std::string fullName =  savePath.append("/portalArrangement.csv");
    saveFile.open(fullName);

    // Check that the save file opened
    if (saveFile.is_open())
    {
        // write the header
        for (size_t i = 0; i < data.size(); i++)
        {
            saveFile << "X" + std::to_string(i) + ", Y" + std::to_string(i) + ", ";
        }

        saveFile << std::endl;

        // write to the save file
        for (size_t i = 0;
             i < data.size();
             i++)
        {
            for (size_t j = 0; j < data[i].size(); j++)
            {
                saveFile << data[i][j] << ", ";
            }
            saveFile << std::endl;
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